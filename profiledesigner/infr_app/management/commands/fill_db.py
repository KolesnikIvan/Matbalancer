import random
import faker

from django.core.management.base import BaseCommand

from infr_app.models import (
    FLOOD_OBJ_TYPES,
    SEP_OBJ_TYPES,
    SeparationObject,
    FloodingObject,
    Well,
    Pad,
    PadDNSConnection,
    PadKNSConnection,
    Field,
    DO,
    WellPadConnection,
    PadFieldConnection,
    DNSFieldConnection,
    KNSFieldConnection,
    DNSKNSConnection,
    KNSDNSConnection,
    Prognose,
)

fake = faker.Faker()

DO_NUM = 10
FIELD_NUM = 90
PAD_NUM = random.randint(10, 120)    #(80, 330)
WELL_NUM = PAD_NUM * random.randint(3, 20)# 24)
DNS_NUM = int(PAD_NUM * random.randint(1, 3) / 30)
KNS_NUM = int(PAD_NUM * random.randint(1, 3) / 30)


class Command(BaseCommand):
    
    def handle(self, *args, **options):
        # import pdb; pdb.set_trace()
        # self._create_objects(DO, ("name",), (fake.country()+ "Oil Inc.",), DO_NUM)
        # self._create_objects(Field, ("name", "do"), (fake.country()+ "field", random.randint(0, 1)), FIELD_NUM)

        self.create_do()
        self.create_field()
        for _ in range(FIELD_NUM):
            self._create_pads()
            self._create_sources()
            self.create_dns()
            self.create_kns()

    def create_do(self):
        for _ in range(DO_NUM):
            new_do = DO(
                name=fake.country() + "Oil Inc.",
            )
            new_do.save()

    def create_field(self):
        for _ in range(FIELD_NUM):
            new_do = Field(
                name=fake.country()+ "_field",
                do=random.choice(DO.objects.all())
            )
            new_do.save()
                    
    # def _create_objects(self, cls_, attrs: tuple, values: tuple, num:int) -> None:
    #     for _ in range(1, num+1):
    #         for k, v in zip(attrs, values):
    #             obj_ = cls_()
    #             setattr(obj_, k, eval(v))
    #             obj_.save()
        
    def _create_pads(self):
        names = self.__create_names(PAD_NUM)
        liq_t, oil_t, gas_t, flood_t = self.__create_flows(PAD_NUM)
        for nm, liq, oil, gas, flood in zip(names, liq_t, oil_t, gas_t, flood_t):
            new_pad = Pad(
                name=nm,
                liq_fact=liq,
                oil_fact=oil,
                gas_fact=gas,
                fld_fact=flood,                
            )
            new_pad.save()

    def _create_sources(self):
        names = self.__create_names(WELL_NUM)
        dests = list()
        for _ in range(WELL_NUM):
            if random.random() < 0.5:
                dests.append("prod")
            else:
                dests.append("inj")
        liq_t, oil_t, gas_t, flood_t = self.__create_flows(WELL_NUM)
        for nm, dst, liq, oil, gas, flood in zip(names, dests, liq_t, oil_t, gas_t, flood_t):
            new_well = Well(\
                name=nm,
                dest=dst,
                liq_fact=liq,
                oil_fact=oil,
                gas_fact=gas,
                fld_fact=flood,
                pad=random.choice(Pad.objects.all()),    # random.randint(1, PAD_NUM),
                # field=random.randint(1,FIELD_NUM),
                )
            new_well.save()

    def create_dns(self):
        for _ in range(DNS_NUM):
            new_dns = SeparationObject(
                name=str(fake.city()),
                obj_type=random.choice(SEP_OBJ_TYPES)[0],
                liq_sep_pwr=random.randint(60, 600)*10,
                oil_sep_pwr=random.randint(30,70)*10,
                wat_sep_pwr=random.randint(60,300)*10,
                liq_pmp_pwr=random.choice((60,120,180,240))*24/1000,
                oil_pmp_pwr=random.choice((60,120,180,240))*24/1000,
                wat_pmp_pwr=random.choice((60,120,180,240))*24/1000,
                wcut=random.randint(1, 10),
                field=random.choice(Field.objects.all()),
            )
            new_dns.save()

    def create_kns(self):
        """KNSs"""
        for _ in range(KNS_NUM):
            new_kns = FloodingObject(
                name=fake.city(),
                field=random.choice(Field.objects.all()),
                obj_type=random.choice(FLOOD_OBJ_TYPES)[0],
                wat_pmp_pwr=random.choice((60,120,180,240))*24/1000,
                wat_src_dbt=random.randint(80, 160),
            )
            new_kns.save()

    def __create_names(self, length):
        names = set()
        while len(names) < length:
            if random.random() < 0.5:
                names.add(str(random.randint(1,350)))
            else:
                names.add(str(random.randint(1,350)) + fake.random_element())
        return names
    
    def __create_flows(self, length):
        liq_t, oil_t, gas_t, flood_t = list(), list(), list(), list()
        for _ in range(length):
            liq = random.randint(1, 100)
            oil = liq * random.randint(20,60) // 100
            gas = oil * (random.randint(30,80))
            flood = liq * random.randint(100,130) / 100
            liq_t.append(liq)
            oil_t.append(oil)
            gas_t.append(gas)
            flood_t.append(flood)
        return liq_t, oil_t, gas_t, flood_t
    