from datetime import datetime, timedelta
from client import Client
from service import Service
from staff import Staff
from appointment import Appointment
from payment import Payment
from premium_client import PremiumClient

def main():
    # Создаём клиента
    client = Client("Молодой", 28, "Мужской", "Иван", "Решительный")
    client.show_basic_info()
    print("Категория:", client.get_age_category())
    client.update_behavior("Активное")
    print()

    # Создаём VIP клиента (наследник)
    vip_client = PremiumClient("Премиум", 40, "Женский", "Алина", "Общительная", "Platinum")
    vip_client.show_basic_info()
    print()

    # Создаём услугу
    service = Service("Стрижка", 1500, "1 час", ["классическая", "комфорт"])
    service.show_service_info()
    service.apply_promotion("Скидка 15%")
    print("Цена со скидкой 20%:", service.get_discounted_price(20))
    print()

    # Создаём персонал
    staff_member = Staff("Парикмахер", 5, 9, 8, "Стрижка аккуратная")
    staff_member.answer_questions()
    staff_member.update_experience(6)
    print("Уровень профессионализма:", staff_member.get_professional_level())
    print()

    # Создаём запись на приём
    appointment_time = datetime.now() + timedelta(days=3)
    appointment = Appointment(appointment_time)
    appointment.show_info()
    appointment.change_date_time(appointment_time + timedelta(days=1))
    print("Прошло ли время записи:", appointment.is_past())
    print()

    # Создаём оплату
    payment = Payment(True, "Карта", False, 1500)
    payment.show_payment_info()
    payment.update_amount(1600)
    print("Полная оплата:", payment.is_full_payment())
    print()

if __name__ == "__main__":
    main()
