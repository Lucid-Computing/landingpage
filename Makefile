.PHONY: fetch-main merge-main push-main update-posts publish

# Fetch latest changes from main branch
fetch-main:
	@echo "Fetching latest from main..."
	git fetch origin main

# Merge main into current branch
merge-main:
	@echo "Merging main into current branch..."
	git merge origin/main || true

# Push current branch to main
push-main:
	@echo "Pushing current branch to main..."
	git push origin HEAD:main

# Update posts.json with published posts
update-posts:
	@echo "Updating blog/posts.json with published posts..."
	python3 update_posts.py

# Combined command: fetch from main, merge, update posts, and push to main
publish: fetch-main merge-main update-posts push-main
	@echo "Publish workflow completed!"
