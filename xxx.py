try:
    if self.permission_1 not in self.permission_modes or self.permission_1 not in self.permission_modes or \
            self.permission_1 < 800 or self.permission_2 < 600 or len(self.permission_1) == 1:
        self.label_Error.show()
except Exception as e:
    self.label_Error.show()
else:
    if self.permission == -1:
        self.label_Error.show()
print(len(self.permission_1), self.permission_2, self.permission)