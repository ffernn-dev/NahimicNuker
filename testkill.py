import psutil

print("NahimicService.exe" in (p.name() for p in psutil.process_iter()))