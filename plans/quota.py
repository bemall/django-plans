def get_user_quota(user):
    """
    Tiny helper for getting quota dict for user
    If user has expired plan, return def plan or None
    """
    from .models import Plan
    plan = Plan.get_current_plan(user)
    return plan.get_quota_dict()
