"""
Test /cohort/user
"""
import re
from unittest.mock import patch
from django.urls.base import reverse_lazy
from rest_framework import status
from breathecode.tests.mocks import (
    GOOGLE_CLOUD_PATH,
    apply_google_cloud_client_mock,
    apply_google_cloud_bucket_mock,
    apply_google_cloud_blob_mock,
)
from ..mixins import AdmissionsTestCase

class CohortUserTestSuite(AdmissionsTestCase):
    """Test /cohort/user"""

    def test_cohort_user_without_auth(self):
        """Test /cohort/user without auth"""
        url = reverse_lazy('admissions:cohort_user')
        response = self.client.get(url)
        json = response.json()

        self.assertEqual(json, {
            'detail': 'Authentication credentials were not provided.',
            'status_code': status.HTTP_401_UNAUTHORIZED
        })
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_cohort_user_without_data(self):
        """Test /cohort/user without auth"""
        url = reverse_lazy('admissions:cohort_user')
        self.generate_models(authenticate=True)
        response = self.client.get(url)
        json = response.json()

        self.assertEqual(json, [])
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    @patch(GOOGLE_CLOUD_PATH['client'], apply_google_cloud_client_mock())
    @patch(GOOGLE_CLOUD_PATH['bucket'], apply_google_cloud_bucket_mock())
    @patch(GOOGLE_CLOUD_PATH['blob'], apply_google_cloud_blob_mock())
    def test_cohort_user_with_data(self):
        """Test /cohort/user without auth"""
        url = reverse_lazy('admissions:cohort_user')
        self.generate_models(authenticate=True, cohort_user=True)
        response = self.client.get(url)
        json = response.json()
        print(json)
        expected = [{
            'role': self.cohort_user.role,
            'finantial_status': self.cohort_user.finantial_status,
            'educational_status': self.cohort_user.educational_status,
            'created_at': re.sub(r'\+00:00$', 'Z', self.cohort_user.created_at.isoformat()),
            'cohort': {
                'id': self.cohort_user.cohort.id,
                'kickoff_date': self.cohort_user.cohort.kickoff_date,
                'name': self.cohort_user.cohort.name,
                'slug': self.cohort_user.cohort.slug,
                'stage': self.cohort_user.cohort.stage,
            },
            'user': {
                'id': self.cohort_user.user.id,
                'first_name': self.cohort_user.user.first_name,
                'last_name': self.cohort_user.user.last_name,
                'email': self.cohort_user.user.email,
            },
        }]

        self.assertEqual(json, expected)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    @patch(GOOGLE_CLOUD_PATH['client'], apply_google_cloud_client_mock())
    @patch(GOOGLE_CLOUD_PATH['bucket'], apply_google_cloud_bucket_mock())
    @patch(GOOGLE_CLOUD_PATH['blob'], apply_google_cloud_blob_mock())
    def test_cohort_user_with_data_with_bad_roles(self):
        """Test /cohort/user without auth"""
        self.generate_models(authenticate=True, cohort_user=True)
        base_url = reverse_lazy('admissions:cohort_user')
        url = f'{base_url}?roles=they-killed-kenny'
        response = self.client.get(url)
        json = response.json()

        self.assertEqual(json, [])
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    @patch(GOOGLE_CLOUD_PATH['client'], apply_google_cloud_client_mock())
    @patch(GOOGLE_CLOUD_PATH['bucket'], apply_google_cloud_bucket_mock())
    @patch(GOOGLE_CLOUD_PATH['blob'], apply_google_cloud_blob_mock())
    def test_cohort_user_with_data_with_roles(self):
        """Test /cohort/user without auth"""
        self.generate_models(authenticate=True, cohort_user=True)
        base_url = reverse_lazy('admissions:cohort_user')
        url = f'{base_url}?roles={self.cohort_user.role}'
        response = self.client.get(url)
        json = response.json()
        print(json)
        expected = [{
            'role': self.cohort_user.role,
            'finantial_status': self.cohort_user.finantial_status,
            'educational_status': self.cohort_user.educational_status,
            'created_at': re.sub(r'\+00:00$', 'Z', self.cohort_user.created_at.isoformat()),
            'cohort': {
                'id': self.cohort_user.cohort.id,
                'kickoff_date': self.cohort_user.cohort.kickoff_date,
                'name': self.cohort_user.cohort.name,
                'slug': self.cohort_user.cohort.slug,
                'stage': self.cohort_user.cohort.stage,
            },
            'user': {
                'id': self.cohort_user.user.id,
                'first_name': self.cohort_user.user.first_name,
                'last_name': self.cohort_user.user.last_name,
                'email': self.cohort_user.user.email,
            },
        }]

        self.assertEqual(json, expected)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    @patch(GOOGLE_CLOUD_PATH['client'], apply_google_cloud_client_mock())
    @patch(GOOGLE_CLOUD_PATH['bucket'], apply_google_cloud_bucket_mock())
    @patch(GOOGLE_CLOUD_PATH['blob'], apply_google_cloud_blob_mock())
    def test_cohort_user_with_data_with_bad_finantial_status(self):
        """Test /cohort/user without auth"""
        self.generate_models(authenticate=True, cohort_user=True)
        base_url = reverse_lazy('admissions:cohort_user')
        url = f'{base_url}?finantial_status=they-killed-kenny'
        response = self.client.get(url)
        json = response.json()

        self.assertEqual(json, [])
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    @patch(GOOGLE_CLOUD_PATH['client'], apply_google_cloud_client_mock())
    @patch(GOOGLE_CLOUD_PATH['bucket'], apply_google_cloud_bucket_mock())
    @patch(GOOGLE_CLOUD_PATH['blob'], apply_google_cloud_blob_mock())
    def test_cohort_user_with_data_with_finantial_status(self):
        """Test /cohort/user without auth"""
        # TODO finantial status in generate models
        self.generate_models(authenticate=True, cohort_user=True, finantial_status='LATE')
        base_url = reverse_lazy('admissions:cohort_user')
        print(self.cohort_user.finantial_status)
        url = f'{base_url}?finantial_status={self.cohort_user.finantial_status}'
        response = self.client.get(url)
        json = response.json()
        print(json)
        expected = [{
            'role': self.cohort_user.role,
            'finantial_status': self.cohort_user.finantial_status,
            'educational_status': self.cohort_user.educational_status,
            'created_at': re.sub(r'\+00:00$', 'Z', self.cohort_user.created_at.isoformat()),
            'cohort': {
                'id': self.cohort_user.cohort.id,
                'kickoff_date': self.cohort_user.cohort.kickoff_date,
                'name': self.cohort_user.cohort.name,
                'slug': self.cohort_user.cohort.slug,
                'stage': self.cohort_user.cohort.stage,
            },
            'user': {
                'id': self.cohort_user.user.id,
                'first_name': self.cohort_user.user.first_name,
                'last_name': self.cohort_user.user.last_name,
                'email': self.cohort_user.user.email,
            },
        }]

        self.assertEqual(json, expected)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    @patch(GOOGLE_CLOUD_PATH['client'], apply_google_cloud_client_mock())
    @patch(GOOGLE_CLOUD_PATH['bucket'], apply_google_cloud_bucket_mock())
    @patch(GOOGLE_CLOUD_PATH['blob'], apply_google_cloud_blob_mock())
    def test_cohort_user_put_without_id(self):
        """Test /cohort/user without auth"""
        url = reverse_lazy('admissions:cohort_user')
        self.generate_models(authenticate=True)
        data = {}
        response = self.client.put(url, data)
        json = response.json()
        print(json)

        self.assertEqual(json, {'status_code': 400, 'details': 'Missing user_id or cohort_id'})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
