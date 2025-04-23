class OtpAuth:
    generated_otp_code = None

    def __init__(self, otp_range=5):
        self.otp_range = otp_range

    def run(self):
        pass

    def otp_handler(self):
        self.generated_otp_code = self.generate_otp_by_length()



    def generate_otp_by_length(self):
        if self.otp_range == 4:
            otp_code = self.generate_otp(1000, 9999)
        elif self.otp_range == 5:
            otp_code = self.generate_otp(10000, 99999)
        elif self.otp_range == 6:
            otp_code = self.generate_otp(100000, 999999)

        else:
            raise ValueError("OTP range must be one of the following: 4, 5, or 6.")

        return otp_code


    @staticmethod
    def generate_otp(start, end):
        import random
        return random.randint(start, end)


    def store_generated_otp_in_cache(self, otp):
        pass