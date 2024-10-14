from django.shortcuts import render, get_object_or_404, redirect
from .models import Job, Bid
from .forms import JobForm, BidForm

def job_list(request):
    jobs = Job.objects.all()  # Fetch all available jobs
    return render(request, 'jobs/job_list.html', {'jobs': jobs})

def job_detail(request, job_id):
    job = get_object_or_404(Job, pk=job_id)
    bids = job.bid_set.all()  # Fetch all bids for the job
    return render(request, 'jobs/job_detail.html', {'job': job, 'bids': bids})

def create_job(request):
    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            job = form.save(commit=False)
            job.client = request.user  # Assuming the logged-in user is a client
            job.save()
            return redirect('job_list')
    else:
        form = JobForm()
    return render(request, 'jobs/create_job.html', {'form': form})

def bid_on_job(request, job_id):
    job = get_object_or_404(Job, pk=job_id)
    if request.method == 'POST':
        form = BidForm(request.POST)
        if form.is_valid():
            bid = form.save(commit=False)
            bid.job = job
            bid.freelancer = request.user  # Assuming the logged-in user is a freelancer
            bid.save()
            return redirect('job_detail', job_id=job.id)
    else:
        form = BidForm()
    return render(request, 'jobs/bid_on_job.html', {'form': form, 'job': job})

