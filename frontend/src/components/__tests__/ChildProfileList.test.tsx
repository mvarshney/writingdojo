import React from 'react';
import { render, screen, fireEvent } from '@testing-library/react';
import { MemoryRouter } from 'react-router-dom';
import ChildProfileList from '../ChildProfileList';

// Mock the API calls
jest.mock('../../api/childProfiles', () => ({
  getChildProfiles: jest.fn().mockResolvedValue([
    {
      id: 1,
      name: 'Test Child 1',
      age: 10,
      grade_level: '5th grade',
      interests: ['reading', 'writing'],
      learning_goals: ['improve grammar']
    },
    {
      id: 2,
      name: 'Test Child 2',
      age: 12,
      grade_level: '7th grade',
      interests: ['science', 'math'],
      learning_goals: ['better essays']
    }
  ])
}));

describe('ChildProfileList', () => {
  it('renders the list of child profiles', async () => {
    render(
      <MemoryRouter>
        <ChildProfileList />
      </MemoryRouter>
    );

    // Wait for the profiles to load
    const profile1 = await screen.findByText('Test Child 1');
    const profile2 = await screen.findByText('Test Child 2');

    expect(profile1).toBeInTheDocument();
    expect(profile2).toBeInTheDocument();
  });

  it('displays profile details correctly', async () => {
    render(
      <MemoryRouter>
        <ChildProfileList />
      </MemoryRouter>
    );

    // Wait for the profiles to load
    await screen.findByText('Test Child 1');

    // Check profile details
    expect(screen.getByText('Age: 10')).toBeInTheDocument();
    expect(screen.getByText('Grade: 5th grade')).toBeInTheDocument();
    expect(screen.getByText('Interests: reading, writing')).toBeInTheDocument();
    expect(screen.getByText('Goals: improve grammar')).toBeInTheDocument();
  });

  it('handles profile selection', async () => {
    const onSelectProfile = jest.fn();
    
    render(
      <MemoryRouter>
        <ChildProfileList onSelectProfile={onSelectProfile} />
      </MemoryRouter>
    );

    // Wait for the profiles to load
    const profile1 = await screen.findByText('Test Child 1');

    // Click on a profile
    fireEvent.click(profile1);

    // Check if the callback was called with the correct profile
    expect(onSelectProfile).toHaveBeenCalledWith({
      id: 1,
      name: 'Test Child 1',
      age: 10,
      grade_level: '5th grade',
      interests: ['reading', 'writing'],
      learning_goals: ['improve grammar']
    });
  });

  it('handles loading state', () => {
    render(
      <MemoryRouter>
        <ChildProfileList />
      </MemoryRouter>
    );

    // Check if loading indicator is shown
    expect(screen.getByText('Loading...')).toBeInTheDocument();
  });

  it('handles error state', async () => {
    // Mock API error
    jest.spyOn(require('../../api/childProfiles'), 'getChildProfiles')
      .mockRejectedValueOnce(new Error('Failed to fetch profiles'));

    render(
      <MemoryRouter>
        <ChildProfileList />
      </MemoryRouter>
    );

    // Wait for error message
    const errorMessage = await screen.findByText('Error loading profiles');
    expect(errorMessage).toBeInTheDocument();
  });
}); 